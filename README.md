# 시간 추적 클래스(TimeTracker)


시간을 관리하고 추적하는 TimeTracker 클래스를 구현하는 프로젝트를 시작합니다. 시간 관리 기능은 특히 프로젝트 작업, 운동, 공부 시간 등 다양한 활동의 지속 시간을 측정하는 데 유용합니다.


  `TimeTracker` 클래스는 다음 기능을 제공합니다:

  1. **시작 시간 설정**: 사용자가 활동을 시작할 때의 시간을 기록합니다.
  2. **종료 시간 설정**: 사용자가 활동을 종료할 때의 시간을 기록합니다.
  3. **경과 시간 계산**: 활동의 시작과 종료 사이의 시간 차이를 계산합니다.

  이 클래스의 인스턴스를 사용하여 각각의 활동에 대해 별도의 시간 추적을 할 수 있습니다.


- 구현 메소드
  
  - `start`: 현재 시간을 시작 시간으로 설정합니다.
  - `stop`: 현재 시간을 종료 시간으로 설정하고 경과 시간을 계산합니다.
  - `get_elapsed_time`: 마지막으로 기록된 시작 시간과 종료 시간 사이의 경과 시간을 분 단위로 반환합니다.
