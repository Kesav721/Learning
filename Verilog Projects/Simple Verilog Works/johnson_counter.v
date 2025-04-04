module johnson_counter(clk,clr,init,count);
input clk,clr,init;
output reg [3:0]count;
always @(posedge clk)
begin
if (clr)
count=4'bxxxx;
else if(init)
count=4'b0000;
else 
count={~count[0],count[3:1]};
end
endmodule