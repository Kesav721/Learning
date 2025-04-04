module zero_detector_tb();
reg [7 : 0] num;
wire is_zero; 
zero_detector DUT(.num(num),.is_zero(is_zero));
initial begin 
$dumpfile("zero_detector.vcd");
$dumpvars(0,zero_detector_tb);
$monitor($time,"num=%b,is_zero=%b",num,is_zero);
end 
initial begin 
num =8'b00000000;
#5 num= 8'b0000001;
#5 num = 8'b00000010;
#5 num = 8'b00000000;
#5 num = 8'b00001100;
#5 num = 8'b01010011;
#5 num = 8'b00000000;
#5 num = 8'b00000000;
$finish;
end
endmodule