module bcd_to_7_seg_tb();
reg [3:0]binary;
wire [6:0]seg;
integer i;
bcd_to_7_seg DUT(.binary(binary),.seg(seg));
initial
begin
for(i=0;i<10;i=i+1)
begin
binary=i;
#15;
end
#15;$finish;
end
initial
begin
$monitor("value of abcdefg=%b",seg);
end
endmodule