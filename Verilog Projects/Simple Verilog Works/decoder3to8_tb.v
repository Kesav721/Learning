module decoder_3to8_tb;
reg [2:0]A,B,C;
wire G0,G1,G2,G3,G4,G5,G6,G7;
decoder_3to8 DUT (A,B,C,G0,G1,G2,G3,G4,G5,G6,G7);
initial 
begin 
$dumpfile("decoder_3to8.vcd");
$dumpvars(0,decoder_3to8_tb);
$monitor($time,"A=%b,B=%b,C=%b,G0=%b,G1=%b,G2=%b,G3=%b,G4=%b,G5=%b,G6=%b,G7=%b",A,B,C,G0,G1,G2,G3,G4,G5,G6,G7);

#4 A=0;B=0;C=0;
#4 A=0;B=0;C=1;
#4 A=0;B=1;C=0;
#4 A=0;B=1;C=1;
#4 A=1;B=0;C=0;
#4 A=1;B=0;C=1;
#4 A=1;B=1;C=0;
#4 A=1;B=1;C=1;
#4 $finish;
end
endmodule