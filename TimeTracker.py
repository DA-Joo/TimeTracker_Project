from datetime import datetime

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        # 현재 시간을 시작 시간으로 설정합니다.
        self.start_time = datetime.now()
        print(f"활동 시작 시간: {self.start_time}")

    def stop(self):
        # 현재 시간을 종료 시간으로 설정하고 경과 시간을 계산합니다.
        if self.start_time is None:
            raise ValueError("활동이 시작되지 않았습니다. 먼저 start() 메소드를 호출하세요.")
        self.end_time = datetime.now()
        print(f"활동 종료 시간: {self.end_time}")

    def get_elapsed_time(self):
        # 마지막으로 기록된 시작 시간과 종료 시간 사이의 경과 시간을 분 단위로 반환합니다.
        if self.start_time is None or self.end_time is None:
            raise ValueError("활동이 시작되거나 종료되지 않았습니다. start() 및 stop() 메소드를 호출하세요.")

        # 경과 시간을 분 단위로 변환
        elapsed_time = (self.end_time - self.start_time).total_seconds() / 60

         # 소수점 둘째 자리까지 반올림하여 반환
        return round(elapsed_time, 2)

study_session = TimeTracker()
study_session.start()

study_session.stop()

print("공부한 시간:", study_session.get_elapsed_time(), "분")
