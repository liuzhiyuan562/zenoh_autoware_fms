

import zenoh

GET_POSE_KEY_EXPR = '/api/vehicle/kinematics'
GET_GOAL_POSE_KEY_EXPR = '/api/routing/route'
SET_AUTO_MODE_KEY_EXPR = '/api/operation_mode/change_to_autonomous'
SET_ROUTE_POINT_KEY_EXPR = '/api/routing/set_route_points'
SET_CLEAR_ROUTE_KEY_EXPR = '/api/routing/clear_route'


class PoseServer:
    def __init__(self, session):
        self.session = session
        self.vehicles = {}
    
    def find_vehicles(self, time=10):
        for scope, vehicle in self.vehicles.items():
            vehicle.subscriber_pose.undeclare()
        self.vehicles = {}
        for _ in range(time):
            replies = self.session.get('@/**/ros2/**' + )


if __name__ == '__main__':
    conf = zenoh.Config.from_file('config.json5')
    session = zenoh.open(conf)
