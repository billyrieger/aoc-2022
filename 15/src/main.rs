use std::collections::HashMap;

use glam::IVec2;
use regex::Regex;

use anyhow::Result;

fn dist(a: IVec2, b: IVec2) -> i32 {
    let v = (a - b).abs();
    v.x + v.y
}

fn main() -> Result<()> {
    let file = std::fs::read_to_string(std::env::args().nth(1).unwrap())?;
    let re = Regex::new(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)")?;
    let mut data = HashMap::new();
    let (mut x_min, mut x_max) = (i32::MAX, i32::MIN);
    for cap in re.captures_iter(&file) {
        let sensor = IVec2::new(cap[1].parse()?, cap[2].parse()?);
        let beacon = IVec2::new(cap[3].parse()?, cap[4].parse()?);
        x_min = x_min.min(sensor.x).min(beacon.x);
        x_max = x_max.max(sensor.x).max(beacon.x);
        data.insert(sensor, beacon);
    }
    let width = x_max - x_min;

    // let y = 10;
    let y = 2000000;
    let mut count = 0;
    for x in (x_min - width)..(x_max + width) {
        let pos = IVec2::new(x, y);
        if data
            .iter()
            .any(|(&sensor, &beacon)| dist(sensor, pos) <= dist(sensor, beacon) && pos != beacon)
        {
            count += 1;
        }
    }
    println!("part 1: {count}");

    Ok(())
}
