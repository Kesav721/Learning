module decoder_3to8(A,B,C,G0,G1,G2,G3,G4,G5,G6,G7);
input[2:0]A,B,C;
output G0,G1,G2,G3,G4,G5,G6,G7;
assign G0=(~A&~B&~C);
assign G1=(~A&~B&C);
assign G2=(~A&B&~C);
assign G3=(~A&B&C);
assign G4=(A&~B&~C);
assign G5=(A&~B&C);
assign G6=(A&B&~C);
assign G7=(A&B&C);
endmodule