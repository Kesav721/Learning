module priority_encoder_tb();
reg [7:0]d;
wire [2:0]y;
priority_encoder DUT(.d(d),.y(y));

initial begin 
$dumpfile("priority_encoder.vcd");
$dumpvars(0,priority_encoder_tb);
$monitor($time,"d=%b,y=%b",d,y);
d=8'b00000000;
#5 d=8'b00000001 ;
#5 d=8'b00000010 ;
#5 d=8'b00000100 ;
#5 d=8'b00001000 ;
#5 d=8'b00010000 ;
#5 d=8'b00100000 ;
#5 d=8'b01000000 ;
#5 d=8'b10000000 ;
#5 d=8'b11111111 ;
#5 $finish;
end
endmodule