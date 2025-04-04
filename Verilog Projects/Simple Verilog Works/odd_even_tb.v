module odd_even_tb();
reg [3:0]num;
wire even,odd;

odd_even DUT (.num(num),.even(even),.odd(odd));
initial begin 
$dumpfile("odd_even.vcd");
$dumpvars(0,odd_even_tb);
$monitor($time,"num=%b,odd=%b,even=%b",num,even,odd);
end
initial begin
num=4'b0000;
#5 num=4'b0001;
#5 num=4'b0010;
#5 num=4'b0011;
#5 num=4'b0100;
#5 num=4'b0101;
#5 num=4'b0110;
#5 num=4'b0111;
#5 num=4'b1000;
#5 num=4'b1001;
$finish;
end
endmodule