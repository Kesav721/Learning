
module odd_even(num,even,odd);
input [3:0]num;
output reg even,odd;

always @ (*) begin
even = ~num[0];
odd  =  num[0];
end
endmodule
