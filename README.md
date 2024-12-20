##  Attendance Management System Using Face Recognition

## **Overview**
This project is an AI-powered attendance management system that uses face recognition to automate the process of recording attendance. The system captures real-time facial data, matches it with stored records, and marks attendance efficiently.

---

## **Features**
- Face recognition using advanced models.
- Real-time attendance marking.
- Secure data storage and management.
- User-friendly interface.
- Multi-platform compatibility (web, mobile, desktop).
- Notification system (email/SMS alerts).

---

## **Technologies Used**
- **Programming Language:** Python
- **Frameworks:** Flask/Django
- **Libraries:** OpenCV, TensorFlow/Keras, dlib, NumPy, Pandas
- **Database:** MySQL/PostgreSQL
- **Frontend:** HTML, CSS, JavaScript

---

## **Installation and Setup**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/kranthi90597/attendance-management-system.git
   cd attendance-management-system
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate    # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup the database:**
   - Configure database credentials in `config.py`.
   - Run database migrations.

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open a web browser and go to `http://localhost:5000`

---

## **Usage**
1. Register new users with facial images.
2. Start the face recognition system.
3. The system automatically marks attendance when a face is recognized.
4. View attendance records and generate reports.

---

## **Project Structure**
```
attendance-management-system/
│── app.py                # Main application file
│── config.py             # Configuration file
│── models/               # Machine learning models
│── static/               # Static files (CSS, JS, images)
│── templates/            # HTML templates
│── database/             # Database models and migrations
│── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```


## **Acknowledgments**
- OpenCV for computer vision functionalities.
- TensorFlow/Keras for deep learning models.
- Flask/Django for backend support.

---

## **Contact**
For any inquiries, feel free to reach out via email:
kranthi90597@gmail.com
