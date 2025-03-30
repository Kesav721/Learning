module uart_rx_controller (
    input wire clk,
    input wire rst,
    input wire rx,
    input wire tick,
    output reg sample,
    output reg receiving
);
    always @(posedge clk or posedge rst) begin
        if (rst) begin
            receiving <= 0;
            sample <= 0;
        end else if (!receiving && rx == 0) begin 
            receiving <= 1;
        end else if (receiving && tick) begin
            sample <= 1;
        end else begin
            sample <= 0;
            if (rx == 1) receiving <= 0; 
        end
    end
endmodule
