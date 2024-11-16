import streamlit as st
import torch
import cv2
import os
import requests
from serpapi import GoogleSearch
from ultralytics import YOLO
from PIL import Image
import tempfile

def detect_objects_yolov5(image_path):
    from ultralytics import YOLO
    
    # Load YOLOv5 model
    model = YOLO('yolov5s.pt')  # Ensure you have yolov5s.pt in the working directory or use a full path

    # Perform inference
    results = model(image_path)

    detected_objects = []
    for result in results:
        for box in result.boxes:
            bbox = box.xyxy.cpu().numpy().astype(int).flatten()  # x1, y1, x2, y2
            conf = float(box.conf.cpu().numpy().flatten()[0])   # Confidence
            cls = int(box.cls.cpu().numpy().flatten()[0])       # Class
            detected_objects.append({
                "bbox": tuple(bbox),
                "confidence": conf,
                "class": cls
            })

    return detected_objects, results

def crop_and_save_object(image, bbox, output_dir, obj_index):
    x1, y1, x2, y2 = bbox
    cropped_img = image[y1:y2, x1:x2]
    output_path = os.path.join(output_dir, f"cropped_object_{obj_index}.png")
    cv2.imwrite(output_path, cropped_img)
    return output_path

def upload_to_imgur(image_path, client_id):
    """ Upload image to Imgur and return the image URL """
    headers = {'Authorization': f'Client-ID {client_id}'}
    with open(image_path, 'rb') as img:
        response = requests.post("https://api.imgur.com/3/image", headers=headers, files={"image": img})

    data = response.json()
    if response.status_code == 200 and data["success"]:
        return data["data"]["link"]
    else:
        st.error(f"Error uploading image to Imgur: {data.get('data', {}).get('error', 'Unknown error')}")
        return None

def perform_google_lens_search(api_key, image_url):
    params = {
        "engine": "google_lens",
        "country": "in",
        "url": image_url,  # Image URL for the Google Lens search
        "api_key": api_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    if "visual_matches" in results:
        return results["visual_matches"]
    else:
        st.error("No visual matches found.")
        return None

def main():
    st.title("Object Detection and Search App")
    st.write("Upload an image, detect objects using YOLOv5, and search for similar items using Google Lens.")

    # api_key = st.text_input("Enter your SerpApi API Key:", type="password")
    # imgur_client_id = st.text_input("Enter your Imgur Client ID:", type="password")

    api_key = "d391abaa4565995bf471c54bb1644750e3f874ae0c8f59a48dfb9ae7e590cc7e"
    imgur_client_id = "2f2e44e79e1f7fb"

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
            temp_file.write(uploaded_file.read())
            image_path = temp_file.name

        # Load the image using OpenCV
        image = cv2.imread(image_path)
        if image is None:
            st.error("Error loading the image. Please upload a valid image file.")
            return

        # Define output directory for cropped objects
        output_dir = tempfile.mkdtemp()  # Create a temporary directory

        # Run object detection
        detected_objects, _ = detect_objects_yolov5(image_path)

        if detected_objects:
            st.write(f"Detected {len(detected_objects)} objects.")
            for i, obj in enumerate(detected_objects):
                bbox = obj["bbox"]
                # Crop and save the object
                cropped_image_path = crop_and_save_object(image, bbox, output_dir, i)

                # Display cropped object
                st.image(cropped_image_path, caption=f"Object {i + 1}", use_column_width=True)

                # Upload cropped image to Imgur
                st.write(f"Uploading Object {i + 1} to Imgur...")
                image_url = upload_to_imgur(cropped_image_path, imgur_client_id)

                if image_url:
                    st.write(f"Imgur Link: {image_url}")
                    
                    # Search using Google Lens API
                    st.write(f"Searching for Object {i + 1}...")
                    visual_matches = perform_google_lens_search(api_key, image_url)

                    if visual_matches:
                        st.write(f"Results for Object {i + 1}:")
                        for match in visual_matches:
                            title = match.get("title", "No title")
                            link = match.get("link", "No link")
                            st.write(f"- **{title}**: [Link]({link})")
        else:
            st.warning("No objects detected in the image.")


if __name__ == "__main__":
    main()