module cyclic_lamp(clock, light);
  input clock;
  output reg [2:0] light;  // Correct bit-order for clarity

  // State encoding using parameters
  parameter s0 = 2'b00, s1 = 2'b01, s2 = 2'b10;
  parameter RED = 3'b100, GREEN = 3'b010, YELLOW = 3'b001;

  reg [1:0] state;  // Correct bit-order

  // Sequential logic: State transition on clock edge
  always @(posedge clock)
  begin
    case (state)
      s0: state <= s1;   // Red → Green
      s1: state <= s2;   // Green → Yellow
      s2: state <= s0;   // Yellow → Red
      default: state <= s0;  // Default to Red
    endcase  
  end

  // Combinational logic: Assign lights based on state
  always @(state)
  begin
    case (state)
      s0: light = RED;    // Red light
      s1: light = GREEN;  // Green light
      s2: light = YELLOW; // Yellow light
      default: light = RED; // Safety default to Red
    endcase
  end
endmodule
