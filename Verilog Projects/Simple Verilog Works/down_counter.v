module down_counter(clk,reset,count);
input clk,reset;
output reg[2:0]count;
always @(posedge clk)
begin
if(reset==1)
count<=3'b111;
else
count<=count -1;
end
endmodule