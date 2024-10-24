import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class WebcamSubscriber(Node):
    def __init__(self):
        super().__init__('webcam_subscriber')
        self.subscription = self.create_subscription(Image, 'webcam_image', self.listener_callback, 10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        cv2.imshow('Webcam', frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = WebcamSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
