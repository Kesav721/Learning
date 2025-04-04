module T_to_SR(T,clk,reset,Q,Qbar);
input T,clk,reset;
output reg Q;
output reg Qbar;
wire S,R;
assign S=(T&~Q);
assign R=(T&Q);

always @(posedge clk or posedge reset) begin
        if (reset) begin
            Q <= 0;
            Qbar <= 1;
        end else begin
            // SR Flip-Flop behavior
            if (S && ~R) begin
                Q <= 1;
                Qbar <= 0;
            end else if (~S && R) begin
                Q <= 0;
                Qbar <= 1;
            end
        end
    end
endmodule