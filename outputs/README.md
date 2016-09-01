
This is the outputs directly, each of the CSV files have properties attached to them as seen below:


- `output_3.csv`:
  - Random action agent without updating the state
  - __Results:__
    - _Successful trips_: 13%
    - _Failed trips_: 87%


- `output_8.csv`:
  - includes Qtable update
  - includes agent state update
  - `update_delay` is 0.1
  - `Q_init` is 2
  - `gamma` is 0.5
  - `alpha` is 0.5
  - `epsilon` is 0.5
  - __Results:__
    - _Successful trips_: 64%
    - _Failed trips_: 36%



- `output_9.csv`:
  - includes Qtable update
  - includes agent state update
  - `update_delay` is 0.1
  - `Q_init` is 2
  - `gamma` is 0.8
  - `alpha` is 0.5
  - `epsilon` is 0.5



- `output_10.csv`:
  - Same as above +
  - `gamma` is 0.25



- `output_11.csv`:
  - Same as above +
  - `gamma` is 0.25
  - `alpha` is 0.75


- `output_12.csv`:
  - Same as above +
  - `gamma` is 0.25
  - `alpha` is 0.75
  - `epsilon` is 0.75


- `output_14.csv`:
  - Same as above +
  - `gamma` is 0.5
  - `alpha` is 0.75
  - `epsilon` is 0.85


- `output_15.csv`:
  - Same as above +
  - `gamma` is 0.4
  - `alpha` is 0.75
  - `epsilon` is 0.85
