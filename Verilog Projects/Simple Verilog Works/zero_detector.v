
module zero_detector(num,is_zero);
input [7:0]num;
output reg is_zero;
always @ (*)
begin 
if ( num == 8'b00000000)
is_zero =1;
else 
is_zero =0;
end
endmodule