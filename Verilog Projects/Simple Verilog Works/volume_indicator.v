module volume_level_indicator(volume_level,leds);
parameter LEVELS =8;
input [LEVELS-1 : 0]volume_level;
output reg [LEVELS-1 :0]leds;
integer i; 
always @(*) begin 
leds=0;
for(i=0 ; i<LEVELS ; i=i+1) begin
if(i<volume_level)
leds[i]=1;
end 
end
endmodule