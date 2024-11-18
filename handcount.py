import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start webcam capture
cap = cv2.VideoCapture(0)

# Hand detection configuration
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        
        # Flip the frame horizontally for a mirrored view
        frame = cv2.flip(frame, 1)
        
        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False
        
        # Process the frame with MediaPipe Hands
        results = hands.process(rgb_frame)
        
        # Draw the hand annotations on the frame
        frame.flags.writeable = True
        total_fingers = 0  # Variable to count fingers on both hands
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Get landmarks for the hand
                landmarks = hand_landmarks.landmark
                
                # Finger tip indices: [4, 8, 12, 16, 20]
                finger_tips = [4, 8, 12, 16, 20]
                thumb_tip = landmarks[4].x
                thumb_ip = landmarks[3].x
                
                # Count fingers for the current hand
                fingers = []
                for tip_idx in finger_tips[1:]:  # Exclude thumb for now
                    if landmarks[tip_idx].y < landmarks[tip_idx - 2].y:  # Compare to the middle joint
                        fingers.append(1)
                    else:
                        fingers.append(0)

                # Thumb check: Check if thumb tip is further away than the IP joint
                if thumb_tip > thumb_ip:
                    fingers.insert(0, 1)
                else:
                    fingers.insert(0, 0)

                # Add the count of this hand's fingers to the total
                total_fingers += sum(fingers)
                
        # Display the total finger count on the frame
        cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

        # Display the frame
        cv2.imshow('Hand Tracking', frame)

        # Check if the window is closed
        if cv2.getWindowProperty('Hand Tracking', cv2.WND_PROP_VISIBLE) < 1:
            break

        # Break on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
