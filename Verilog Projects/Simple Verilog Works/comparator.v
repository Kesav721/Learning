module comparator(A,B,AequalB,greater,lesser);
input[3:0]A,B;
output reg AequalB=0,greater=0,lesser=0;
always @ (*)
begin
     if(A>B)
     begin
     greater=1;
     lesser=0;
     AequalB=0;
     end
     else if(A<B)
     begin 
     greater=0;
     lesser=1;
     AequalB=0;
     end 
     else begin 
     greater=0;
     lesser=0;
     AequalB=1;
     end 
     end

endmodule