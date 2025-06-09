import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30) 

colorizer = rs.colorizer()

print("Starting camera stream...")
profile = pipeline.start(config)

try:
    while True:
        # Wait for a coherent set of frames: depth, color, and motion
        frames = pipeline.wait_for_frames()

        # --- 2a. Get Image Frames (Depth and Color) ---
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        
        if not depth_frame or not color_frame:
            continue # If frames are not available, skip this iteration

        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())
        depth_colormap = np.asanyarray(colorizer.colorize(depth_frame).get_data())

        height, width, _ = color_image.shape
        center_x, center_y = width // 2, height // 2

        # Get the distance at the center of the screen
        # This is our NUMERICAL FEEDBACK
        distance_in_meters = depth_frame.get_distance(center_x, center_y)

        # Draw a circle at the center of the color image
        cv2.circle(color_image, (center_x, center_y), 5, (0, 0, 255), -1)

        # Put the distance text on the color image
        feedback_text = f"{distance_in_meters:.2f} meters"
        cv2.putText(color_image, feedback_text, (center_x + 10, center_y + 5), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        # --- 3. Display the Images ---
        # Stack the two images horizontally for a side-by-side view
        images = np.hstack((color_image, depth_colormap))

        # Show the combined images
        cv2.imshow('RealSense D435i Feedback', images)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # --- 4. Cleanup ---
    print("Stopping camera stream...")
    pipeline.stop()
    cv2.destroyAllWindows()
    print("Stream stopped and windows closed.")