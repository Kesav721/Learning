module ring_counter(clk,init,count);
input clk,init;
output reg[2:0]count;
always @(posedge clk)
begin   
if(init)
count=3'b100;
else 

count={count[1:0],count[2]};

 
end 
endmodule