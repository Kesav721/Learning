module full_adder(A,B,C,sum,carry);
input A,B,C;
output sum,carry;
wire t1,t2,t3;
assign sum=A^B^C;
assign carry=(A&B)|(A&C)|(B&C);
endmodule