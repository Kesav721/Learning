module uart_rx (
    input wire clk,
    input wire rst,
    input wire rx,
    output wire [7:0] data,
    output wire rx_done
);
    wire tick, sample, receiving;

    baud_generator #(.BAUD_RATE(9600), .CLK_FREQ(50000000)) baudgen (
        .clk(clk), .rst(rst), .tick(tick)
    );

    uart_rx_controller controller (
        .clk(clk), .rst(rst), .rx(rx), .tick(tick), .sample(sample), .receiving(receiving)
    );

    uart_rx_shift shift_reg (
        .clk(clk), .rst(rst), .tick(tick), .sample(sample), .rx(rx), 
        .data(data), .done(rx_done)
    );

endmodule
