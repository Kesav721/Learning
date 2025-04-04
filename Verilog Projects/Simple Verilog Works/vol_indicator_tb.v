module volume_level_indicator_tb();

reg [7 : 0] volume_level;
wire [7 : 0] leds;
volume_level_indicator DUT (.volume_level(volume_level),.leds(leds));
initial begin 
$dumpfile("volume_level_indicator.vcd");
$dumpvars(0,volume_level_indicator_tb);
$monitor($time,"volume_level=%b,leds=%b",volume_level,leds);
end 
initial begin 
volume_level =0; #10;
volume_level =1; #10;
volume_level =3; #10;
volume_level =5; #10;
volume_level =8; #10;
volume_level =2; #10;
volume_level =7; #10;
$finish;
end
endmodule