
module counter_with_clock_gating(clk,reset,enable,count);
input clk,reset,enable;
output reg [3:0]count;

wire gated_clk;
reg latch_enable;

always @(posedge clk,posedge reset)begin
if(reset)
latch_enable <= 0;
else 
latch_enable <= enable;
end

assign gated_clk = clk & latch_enable;

always@(posedge gated_clk,posedge reset)begin
if (reset)
count <= 4'b0000;
else 
count <= count+1;
end
endmodule