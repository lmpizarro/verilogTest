module DELAY(X, Y, clk, delay, clr);

  input [7:0] delay;

  input signed [15:0] X;
  output signed [15:0] Y;

  input clk, clr;

  reg signed  [15:0] Delay [255:0];

  integer i;

  assign Y =X-Delay[delay];

  always @(posedge clk or posedge clr)
    begin
      if(clr) 
      begin
	for (i=0; i < 256; i= i + 1) 
	begin
	  Delay[i] = 0;
	end
      end 
      else if (clk) 
      begin
	for (i=delay; i > 0; i= i - 1) 
	begin
	  Delay[i] = Delay[i-1];
	end
	Delay[0] = X;
      end
    end
endmodule

module zero_cross(X, outNP, outPN, out, clk, clr);
input signed [15:0] X;
output outNP, outPN;
output reg out;
input clk, clr;

reg [1:0] curr_state;
reg [1:0] next_state;

localparam STATE_0 =3'd0,
           STATE_1 =3'd1,
           STATE_2 =3'd2,
           STATE_3 =3'd3;

assign outPN = (~X>=0 & curr_state [0]);
assign outNP = (X>=0  & curr_state[1]);

always @(posedge clk)
begin
 if (clr) curr_state <= STATE_0;
 else curr_state <= next_state;
end

always @(*) begin
 case(curr_state)
   STATE_0: begin
    if (X>=0) next_state = STATE_1;
    else next_state = STATE_2; 
   end
   STATE_1: begin
    if (X>=0) next_state = STATE_1;
    else next_state = STATE_0; 
   end
   STATE_2: begin
    if (X>=0) next_state = STATE_1;
    else next_state = STATE_2;
   end
   STATE_3: begin
    next_state = STATE_0;
   end
 endcase
end

always @(posedge outNP or posedge outPN) begin
    if (outNP) out =1'b1;
    else if (outPN) out = 1'b0;
end
endmodule

module cfd(X, Y, thr, clk, clr, dely, divis);
 input [15:0] X;
 output [15:0] Y;
 input [15:0] thr;
 input [7:0] dely;
 input [7:0] divis;
 input clk, clr;
 
 wire [15:0] Xdel, Xdiv, Xdiff;

 assign Xdiv = X>>>divis;
 assign Xdiff = Xdel - Xdiv;
 assign Y = (X>thr) & (Xdiff>0) ;

 DELAY dlay(.X(X), .Y(Xdel), .clk(clk), .delay(dely), .clr(clr));

endmodule
