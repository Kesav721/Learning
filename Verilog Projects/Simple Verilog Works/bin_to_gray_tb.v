module binary_to_gray_tb();
reg A,B,C,D;
wire G3,G2,G1,G0;
binary_to_gray DUT(A,B,C,D,G3,G2,G1,G0);
initial
begin
$dumpfile("binary_to_gray.vcd");
$dumpvars(0,binary_to_gray_tb);
$monitor($time,"A=%b,B=%b,C=%b,D=%b,G3=%b,G2=%b,G1=%b,G0=%b",A,B,C,D,G3,G2,G1,G0);

#5 A=0;B=0;C=0;D=0;//0
#5 A=0;B=0;C=0;D=1;//1
#5 A=0;B=0;C=1;D=0;//2
#5 A=0;B=0;C=1;D=1;//3
#5 A=0;B=1;C=0;D=0;//4
#5 A=0;B=1;C=0;D=1;//5
#5 A=0;B=1;C=1;D=0;//6
#5 A=0;B=1;C=1;D=1;//7
#5 A=1;B=0;C=0;D=0;//8
#5 A=1;B=0;C=0;D=1;//9
#5 A=1;B=0;C=1;D=0;//10
#5 A=1;B=0;C=1;D=1;//11
#5 A=1;B=1;C=0;D=0;//12
#5 A=1;B=1;C=0;D=1;//13
#5 A=1;B=1;C=1;D=0;//14
#5 A=1;B=1;C=1;D=1;//15
#5$finish;
end
endmodule