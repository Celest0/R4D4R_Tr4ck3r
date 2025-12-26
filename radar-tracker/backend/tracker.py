from kalman import KalmanFilter
from simulator import TargetSimulator

kf = KalmanFilter()
sim = TargetSimulator()

def update():
    measurement = sim.step()
    kf.predict()
    kf.update(measurement)
    return {
        "measurement": measurement,
        "estimate": kf.state()
    }
