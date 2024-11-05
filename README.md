# SkyRescueAI
### Overview
SkyRescueAI is an autonomous AI-powered detection system designed to assist in search and rescue operations by identifying individuals in challenging forest environments from aerial drone footage. This project aims to fine-tune YOLOv11 to maximize detection accuracy and speed.

### Methodology
We will use transfer learning to fine-tune YOLOv11 models, testing small, medium, and large model versions to find an optimal balance between accuracy and processing speed. The model will be trained on the HERIDAL Database and the Stanford Drone Dataset, both of which offer diverse, real-world images for robust model performance.

### Goals
- Fine-tune and evaluate YOLOv11 variants for real-time person detection.
- Test the model on drone-captured images in forested environments at altitudes up to 100 meters.
- Measure performance with Mean Average Precision (mAP) and Latency metrics to ensure reliable, real-time detection.

### Datasets
- **HERIDAL Database** – Provides varied, high-resolution aerial images suited for human detection tasks.
- **Stanford Drone Dataset** – Contains drone-captured images over various environments, enriching the model's ability to generalize.

### Future Enhancements
Further optimizations will include image slicing (SAHI) to enhance detail detection and TensorRT for faster inference in real-time applications.
