use std::ops::Range;

use anyhow::{anyhow, Result};
use glam::IVec2;
use regex::Regex;

fn dist(a: IVec2, b: IVec2) -> i32 {
    (a.x - b.x).abs() + (a.y - b.y).abs()
}

#[derive(Debug)]
struct ExcludedRow {
    row_y: i32,
    chunks: Vec<Range<i32>>,
}

impl ExcludedRow {
    fn new(row_y: i32) -> Self {
        Self {
            row_y,
            chunks: vec![],
        }
    }

    fn exclude(&mut self, sensor: IVec2, beacon: IVec2) {
        let radius = dist(sensor, beacon);
        let dy = (self.row_y - sensor.y).abs();
        if dy <= radius {
            let dx = radius - dy;
            self.chunks.push((sensor.x - dx)..(sensor.x + dx + 1));
        }
    }

    fn normalize(&mut self) {
        self.chunks.sort_by_key(|range| range.start);
        'outer: loop {
            for i in 0..(self.chunks.len() - 1) {
                let a = &self.chunks[i];
                let b = &self.chunks[i + 1];
                if a.contains(&b.start) {
                    let new_start = a.start;
                    let new_end = a.end.max(b.end);
                    self.chunks.remove(i + 1);
                    self.chunks[i] = new_start..new_end;
                    continue 'outer;
                }
            }
            break;
        }
    }
}

const MAX_X: i32 = 4000000;

fn main() -> Result<()> {
    let file = std::fs::read_to_string(std::env::args().nth(1).ok_or(anyhow!("no input file"))?)?;
    let re = Regex::new(r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)")?;
    // A list of the coordinates of each sensor and coordinates of the nearest beacon to it.
    let mut sensor_data: Vec<(IVec2, IVec2)> = vec![];
    for cap in re.captures_iter(&file) {
        let sensor = IVec2::new(cap[1].parse()?, cap[2].parse()?);
        let beacon = IVec2::new(cap[3].parse()?, cap[4].parse()?);
        sensor_data.push((sensor, beacon));
    }

    for i in 0..=MAX_X {
        let mut row = ExcludedRow::new(i);
        for &(sensor, beacon) in &sensor_data {
            row.exclude(sensor, beacon);
        }
        row.normalize();
        // part 1
        if i == 2000000 {
            let total_len: usize = row.chunks.iter().map(|chunk| chunk.len()).sum();
            // need to subtract 1 because there's a beacon at (x, y) = (3233556, 2000000).
            println!("part 1: {}", total_len - 1);
        }
        // part 2
        if row.chunks.len() == 2 {
            let beacon_x = row.chunks[0].end as i64;
            let beacon_y = i as i64;
            println!("part 2: {}", beacon_x * MAX_X as i64 + beacon_y);
        }
    }

    Ok(())
}
