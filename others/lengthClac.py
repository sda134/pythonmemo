import sys, math

rpm =int(input('rpm?'))

mins_per_a_year= 60 *24 *365
rev_per_a_year= rpm *mins_per_a_year
rev_per_10years= rev_per_a_year *10

int16_digit= (2**15)    # uint16_max=(2**16)-1
int32_digit= (2**31)    # uint16_max=(2**16)-1

print('10年間で %s 分' % (mins_per_a_year * 10))
print('rpm %s の時、10年間で %s 回転する' % (rpm,rev_per_10years))
print('int16の場合は %s 桁必要' % math.log(rev_per_10years, int16_digit))
print('int32の場合は %s 桁必要' % math.log(rev_per_10years, int32_digit))

