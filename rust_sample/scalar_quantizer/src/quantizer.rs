fn intbits(x: f32) -> u32 {
    let y = x.to_bits();
    //println!("{} -> {}", x, y);
    return y;
}

fn floatbits(x: u32) -> f32 {
    let y = x as f32;
    //println!("{} -> {}", x, y);
    return y;
}

pub fn encode_fp16(x: f32) -> u16 {
    let sign_mask: u32 = 0x80000000;
    //println!("u64: {}", sign_mask);
    let mut fint = intbits(x);
    let sign = fint & sign_mask;
    fint ^= sign;

    let f32infty: u32 = 255 << 23;
    let mut o: u32 = if fint > f32infty { 0x7e00 } else { 0x7c00 };

    let round_mask: u32 = !0xfff;
    let magic: u32 = 15 << 23;

    let mut fscale: f32 = floatbits(fint & round_mask) * floatbits(magic);
    let tmp = floatbits((31 << 23) - 0x1000);
    if fscale > tmp {
        fscale = tmp;
    }
    println!("fscale: {}", fscale);
    println!("round : {}", round_mask);
    println!("intbit: {}", intbits(fscale));
    let fint2: u32 = intbits(fscale) - round_mask;
    
    if fint < f32infty {
        o = fint2 >> 13;
    }
    
    return (o | (sign_mask >> 16)) as u16;
}