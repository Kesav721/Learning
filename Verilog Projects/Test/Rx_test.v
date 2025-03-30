`timescale 1ns/1ps

module uart_rx_tb;
    reg clk, rst;
    reg rx;
    wire [7:0] rx_data;
    wire rx_done;

    // Instantiate UART RX module
    uart_rx uut (
        .clk(clk),
        .rst(rst),
        .rx(rx),
        .data(rx_data),
        .rx_done(rx_done)
    );

    always #10 clk = ~clk; // 50 MHz clock (20 ns period)

    initial begin
        clk = 0;
        rst = 1;
        rx = 1;  // Idle state

        #50 rst = 0;  

        // Send start bit (0)
        #104167 rx = 0;  

        // Send 8-bit data (LSB first) - 8'hA5 = 10100101
        #104167 rx = 1;  // Bit 0
        #104167 rx = 0;  // Bit 1
        #104167 rx = 1;  // Bit 2
        #104167 rx = 0;  // Bit 3
        #104167 rx = 0;  // Bit 4
        #104167 rx = 1;  // Bit 5
        #104167 rx = 0;  // Bit 6
        #104167 rx = 1;  // Bit 7

        // Send stop bit (1)
        #104167 rx = 1;  

        #200000;
        $finish;
    end
endmodule
