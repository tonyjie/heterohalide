import heterocl as hcl
hcl.init()
output_extent_0 = 1524
output_extent_1 = 2548
output_min_0 = 0
output_min_1 = 0
def _all(input, ):
    def stage_0_0(stage_0_s0_y, stage_0_s0_x, input, ):
        return ((input[(stage_0_s0_y + 4), (stage_0_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 25)) + ((input[(stage_0_s0_y + 3), (stage_0_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 20)) + ((input[(stage_0_s0_y + 2), (stage_0_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 15)) + ((input[(stage_0_s0_y + 1), (stage_0_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 10)) + ((input[stage_0_s0_y, (stage_0_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 5)) + ((input[(stage_0_s0_y + 4), (stage_0_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 20)) + ((input[(stage_0_s0_y + 3), (stage_0_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 16)) + ((input[(stage_0_s0_y + 2), (stage_0_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 12)) + ((input[(stage_0_s0_y + 1), (stage_0_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 8)) + ((input[stage_0_s0_y, (stage_0_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((input[(stage_0_s0_y + 4), (stage_0_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 15)) + ((input[(stage_0_s0_y + 3), (stage_0_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 12)) + ((input[(stage_0_s0_y + 2), (stage_0_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 9)) + ((input[(stage_0_s0_y + 1), (stage_0_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 6)) + ((input[stage_0_s0_y, (stage_0_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 3)) + ((input[(stage_0_s0_y + 4), (stage_0_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 10)) + ((input[(stage_0_s0_y + 3), (stage_0_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 8)) + ((input[(stage_0_s0_y + 2), (stage_0_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 6)) + ((input[(stage_0_s0_y + 1), (stage_0_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((input[stage_0_s0_y, (stage_0_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 2)) + ((input[(stage_0_s0_y + 4), stage_0_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 5)) + ((input[(stage_0_s0_y + 3), stage_0_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((input[(stage_0_s0_y + 2), stage_0_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 3)) + (input[stage_0_s0_y, stage_0_s0_x] + (input[(stage_0_s0_y + 1), stage_0_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 2))))))))))))))))))))))))))
    stage_0_0 = hcl.compute(((output_extent_1 + 8), (output_extent_0 + 8), ), lambda stage_0_s0_y, stage_0_s0_x, : stage_0_0(stage_0_s0_y, stage_0_s0_x, input, ), name = "stage_0_0", dtype = hcl.UInt(bits = 16))

    def stage_1_0(stage_1_s0_y, stage_1_s0_x, input, stage_0, ):
        return ((stage_0[(stage_1_s0_y + 4), (stage_1_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 25)) + ((stage_0[(stage_1_s0_y + 3), (stage_1_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 20)) + ((stage_0[(stage_1_s0_y + 2), (stage_1_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 15)) + ((stage_0[(stage_1_s0_y + 1), (stage_1_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 10)) + ((stage_0[stage_1_s0_y, (stage_1_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 5)) + ((stage_0[(stage_1_s0_y + 4), (stage_1_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 20)) + ((stage_0[(stage_1_s0_y + 3), (stage_1_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 16)) + ((stage_0[(stage_1_s0_y + 2), (stage_1_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 12)) + ((stage_0[(stage_1_s0_y + 1), (stage_1_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 8)) + ((stage_0[stage_1_s0_y, (stage_1_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((stage_0[(stage_1_s0_y + 4), (stage_1_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 15)) + ((stage_0[(stage_1_s0_y + 3), (stage_1_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 12)) + ((stage_0[(stage_1_s0_y + 2), (stage_1_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 9)) + ((stage_0[(stage_1_s0_y + 1), (stage_1_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 6)) + ((stage_0[stage_1_s0_y, (stage_1_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 3)) + ((stage_0[(stage_1_s0_y + 4), (stage_1_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 10)) + ((stage_0[(stage_1_s0_y + 3), (stage_1_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 8)) + ((stage_0[(stage_1_s0_y + 2), (stage_1_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 6)) + ((stage_0[(stage_1_s0_y + 1), (stage_1_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((stage_0[stage_1_s0_y, (stage_1_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 2)) + ((stage_0[(stage_1_s0_y + 4), stage_1_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 5)) + ((stage_0[(stage_1_s0_y + 3), stage_1_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((stage_0[(stage_1_s0_y + 2), stage_1_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 3)) + (stage_0[stage_1_s0_y, stage_1_s0_x] + (stage_0[(stage_1_s0_y + 1), stage_1_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 2))))))))))))))))))))))))))
    stage_1_0 = hcl.compute(((output_extent_1 + 4), (output_extent_0 + 4), ), lambda stage_1_s0_y, stage_1_s0_x, : stage_1_0(stage_1_s0_y, stage_1_s0_x, input, stage_0_0, ), name = "stage_1_0", dtype = hcl.UInt(bits = 16))

    def stage_2_0(stage_2_s0_y, stage_2_s0_x, input, stage_1, ):
        return ((stage_1[(stage_2_s0_y + 4), (stage_2_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 25)) + ((stage_1[(stage_2_s0_y + 3), (stage_2_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 20)) + ((stage_1[(stage_2_s0_y + 2), (stage_2_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 15)) + ((stage_1[(stage_2_s0_y + 1), (stage_2_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 10)) + ((stage_1[stage_2_s0_y, (stage_2_s0_x + 4)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 5)) + ((stage_1[(stage_2_s0_y + 4), (stage_2_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 20)) + ((stage_1[(stage_2_s0_y + 3), (stage_2_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 16)) + ((stage_1[(stage_2_s0_y + 2), (stage_2_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 12)) + ((stage_1[(stage_2_s0_y + 1), (stage_2_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 8)) + ((stage_1[stage_2_s0_y, (stage_2_s0_x + 3)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((stage_1[(stage_2_s0_y + 4), (stage_2_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 15)) + ((stage_1[(stage_2_s0_y + 3), (stage_2_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 12)) + ((stage_1[(stage_2_s0_y + 2), (stage_2_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 9)) + ((stage_1[(stage_2_s0_y + 1), (stage_2_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 6)) + ((stage_1[stage_2_s0_y, (stage_2_s0_x + 2)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 3)) + ((stage_1[(stage_2_s0_y + 4), (stage_2_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 10)) + ((stage_1[(stage_2_s0_y + 3), (stage_2_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 8)) + ((stage_1[(stage_2_s0_y + 2), (stage_2_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 6)) + ((stage_1[(stage_2_s0_y + 1), (stage_2_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((stage_1[stage_2_s0_y, (stage_2_s0_x + 1)] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 2)) + ((stage_1[(stage_2_s0_y + 4), stage_2_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 5)) + ((stage_1[(stage_2_s0_y + 3), stage_2_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 4)) + ((stage_1[(stage_2_s0_y + 2), stage_2_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 3)) + (stage_1[stage_2_s0_y, stage_2_s0_x] + (stage_1[(stage_2_s0_y + 1), stage_2_s0_x] * hcl.cast(dtype = hcl.UInt(bits = 16), expr = 2))))))))))))))))))))))))))
    stage_2_0 = hcl.compute((output_extent_1, output_extent_0, ), lambda stage_2_s0_y, stage_2_s0_x, : stage_2_0(stage_2_s0_y, stage_2_s0_x, input, stage_1_0, ), name = "stage_2_0", dtype = hcl.UInt(bits = 16))

    def output_0(output_s0_y, output_s0_x, input, stage_2, ):
        return stage_2[output_s0_y, output_s0_x]
    output_0 = hcl.compute((output_extent_1, output_extent_0, ), lambda output_s0_y, output_s0_x, : output_0(output_s0_y, output_s0_x, input, stage_2_0, ), name = "output_0", dtype = hcl.UInt(bits = 16))

    return output_0
input = hcl.placeholder((2560, 1536, ), name = "input", dtype = hcl.UInt(bits = 16))
s = hcl.create_schedule([input, ], _all)
f = hcl.build(s)
print(hcl.lower(s))
import numpy as np
np_input = np.transpose(np.load("input.npy"), (1, 0))
hcl_input = hcl.asarray(np_input, dtype = hcl.UInt(bits = 16))
output_shape = (2548, 1524)
hcl_out = hcl.asarray(np.zeros(output_shape), dtype = hcl.UInt(bits = 16))
f(hcl_input, hcl_out)
np_out = hcl_out.asnumpy()
np_out = np.transpose(np_out, (1, 0))
np.save("output_heterocl.npy", np_out)
print(hcl.build(s, target = "soda"))