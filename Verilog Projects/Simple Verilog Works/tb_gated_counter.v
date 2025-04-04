module counter_with_clock_gating_tb();
reg clk,reset,enable;
wire [3:0] count;
counter_with_clock_gating DUT (.clk(clk),.reset(reset),.enable(enable),.count(count));

initial begin 
clk=0; 
forever #5 clk=~clk;
end 
initial begin 
reset =1; enable=0;
#15 reset=0;enable=1;
#100 enable=0;
#50 enable=1;
#100 $finish;
end
endmodule