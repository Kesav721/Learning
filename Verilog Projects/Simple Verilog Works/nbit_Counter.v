module nbit_counter(clk,clr,count);
parameter N=8;
input clk,clr;
output reg[0:N-1]count;
always @(negedge clk)
if (clr)
count<=0;
else 
count<=count + 1;
endmodule