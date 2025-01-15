# Buy What You See

A **Streamlit application** that enables users to upload a video, detect objects in selected frames using YOLOv5, and search for similar items online via Google Lens. This project integrates deep learning for object detection and web APIs for seamless e-commerce exploration.

---

## Features

- **Video Upload**: Upload videos in common formats like `.mp4`, `.avi`, `.mov`, and `.mkv`.  
- **Object Detection**: Uses the pre-trained YOLOv5 model to identify objects in video frames.  
- **Frame Selection**: Extracts and processes frames from the video, allowing users to choose a specific frame for analysis.  
- **Imgur Integration**: Cropped objects from frames are uploaded to Imgur for public accessibility.  
- **Google Lens Search**: Automatically performs a visual search for detected objects using Google Lens via the SerpAPI.  
- **E-Commerce Links**: Highlights product links on platforms like Amazon and Flipkart for easy purchasing.  

---

## Demo

![App Screenshot](#)  
*(Add a screenshot or GIF showing the app in action)*  

---

## Installation

1. Clone the repository:  
   ```bash  
   git clone https://github.com/<your-username>/buy-what-you-see.git  
   cd buy-what-you-see  
   ```  

2. Create and activate a virtual environment:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Set up environment variables:  
   - Create a `.env` file in the root directory.  
   - Add the following keys:  
     ```plaintext  
     SERPAPI_API_KEY=<your-serpapi-key>  
     IMGUR_CLIENT_ID=<your-imgur-client-id>  
     ```  

5. Run the application:  
   ```bash  
   streamlit run app.py  
   ```  

---

## Usage

1. **Upload a Video**: Upload any video file from your local machine.  
2. **Select a Frame**: Choose a specific frame for object detection.  
3. **Detect Objects**: The app identifies objects in the frame using YOLOv5.  
4. **Search Items**: Crop detected objects, upload them to Imgur, and search for similar products via Google Lens.  
5. **Buy Online**: View e-commerce links to purchase the identified items.  

---

## Requirements

- **Python 3.8+**  
- **Streamlit**  
- **YOLOv5**  
- **OpenCV**  
- **Torch**  
- **Requests**  
- **dotenv**  

---

## API Keys

### Required APIs  
- **SerpAPI**: To perform Google Lens searches.  
- **Imgur**: To upload cropped object images and generate public URLs.  

Create accounts on [SerpAPI](https://serpapi.com/) and [Imgur](https://imgur.com/) to get the respective API keys.  

---

## Contributing

1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-name`.  
3. Commit your changes: `git commit -m 'Add some feature'`.  
4. Push to the branch: `git push origin feature-name`.  
5. Open a pull request.  

---

## License

This project is licensed under the [MIT License](LICENSE).  

---

## Acknowledgments

- **[Ultralytics](https://github.com/ultralytics/yolov5)** for the YOLOv5 model.  
- **[Streamlit](https://streamlit.io/)** for creating interactive web apps.  
- **[SerpAPI](https://serpapi.com/)** for enabling Google Lens visual search.  
- **[Imgur](https://imgur.com/)** for easy image hosting.  

---

Feel free to contribute and make "Buy What You See" even better!
