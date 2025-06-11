module down_counter_tb();
  reg clk = 0, reset;
  wire [2:0] count;

  // Instantiate the down counter module
  down_counter DUT (
    .clk(clk),
    .reset(reset),
    .count(count)
  );

  // Generate a clock signal (Toggle every 5 time units)
  always 
    #5 clk = ~clk;

  initial begin
    // Dump waveform data for visualization
    $dumpfile("down_counter.vcd");
    $dumpvars(0, down_counter_tb);

    // Monitor signal changes
    $monitor($time, " clk=%b, reset=%b, count=%b", clk, reset, count);

    // Test sequence
    reset = 1;  #10  // Apply reset
    reset = 0;  #150 // Let counter run for 150 time units
    reset = 1;  #10  // Apply reset again

    $finish; // Stop simulation
  end
endmodule
