# ColorPalettes README

## Overview

ColorPalettes is a Python class that provides a collection of predefined color palettes for use in data visualization and design. The class includes methods to retrieve and display these palettes, making it easy to incorporate aesthetically pleasing color schemes into your projects.


## Installation

To use ColorPalettes, you need to have the following Python package installed:


matplotlib

You can install this package using pip:


pip install matplotlib

## Usage

## Initialization

You do not need to create an instance of the ColorPalettes class, as all methods are static and can be called directly on the class.


## Methods

get_palette(palette_name, num_colors)

This method retrieves a specified number of colors from a given palette.


palette_name: The name of the palette to retrieve.
num_colors: The number of colors to retrieve from the palette.

Returns:


A list or dictionary of colors from the specified palette.

Example:


colors = ColorPalettes.get_palette('twilight_blues', 3)
print(colors)

display_palette(palette_name, num_colors)

This method displays a specified number of colors from a given palette using a matplotlib plot.


palette_name: The name of the palette to display.
num_colors: The number of colors to display from the palette.

Example:


ColorPalettes.display_palette('twilight_blues', 4)

get_group_name()

This method returns a list of available palette groups.


Returns:


A list of palette group names.

## Example:


groups = ColorPalettes.get_group_name()
print(groups)

display_group_palettes(group_name)

This method displays all palettes within a specified group using a matplotlib plot.


group_name: The name of the group to display.

## Example:


ColorPalettes.display_group_palettes('Tetracolor')

## Available Palettes

The ColorPalettes class includes a variety of predefined color palettes organized into different groups:


- Tetracolor

twilight_blues
sunset_glow
vintage_vibes
earthy_tones
autumn_hues
primary_burst
muted_greens
ocean_depths
pastel_dreams
neon_flash
royal_purples
soft_pinks
forest_shades
luxury_blues

- Alt Black

alt_black

- Bicolor

lavender_peach
blush_gold
apricot_olive
ivory_teal
sage_coral
lime_pink
sky_bronze
pearl_rose
mint_mustard
ochre_blue
sand_rust
peach_navy
blue_red
lilac_navy
olive_plum
peach_forest
sky_coal
iron_brown
cream_teal
gold_navy
sunset_and_sky
blossom_and_grass
sunshine_and_twilight

- Retro Bicolor

ocean_sunset
forest_rose
vintage_rose
harvest_gold
desert_sunset
autumn_leaves
rustic_red
coral_sea
golden_night
twilight_orange
misty_rose
sky_garden
earthy_tones_retro
cherry_sky
midnight_fire
olive_bark
teal_sun
red_dawn

- Chic Bicolor

ocean_sunrise
autumn_leaves
rose_garden
forest_path
woodland_walk
sunset_boulevard
cherry_blossom
desert_sand
meadow_green
urban_sky
summer_citrus
rustic_charm
spring_meadow
golden_horizon
twilight_sky
deep_sea
lime_twist
red_velvet
steely_resolve
soft_petals
crimson_flame
cool_mist
glacial_blue
autumn_spice
royal_plum

- Tricolor

venetian_sunset
cherry_blossom_petals
mountain_range_view
after_the_rain
stone_wall_moss
calm_lake
forest_light_and_shadow
autumn_leaves_journey
warm_earth_scent
moonlit_sea
sunset_tears
soft_pastels
autumn_breeze
aegean_sea
morning_light_rays
fruit_orchard
plum_orchard

- Gradation Bicolor

vibrant_sunset
golden_horizon
aqua_dream
pink_illusion
electric_blue
emerald_fantasy
lavender_bliss
sunset_glow
cherry_blossom
tropical_breeze
ocean_depths
magenta_mystique
fire_and_ice
lime_burst
peachy_keen
neon_night
teal_surge
berry_delight
crimson_sky
cyan_splash
golden_sunshine
mint_fusion
violet_vibe
blush_bloom
aqua_serenity
rose_gold
neon_splash
silver_mist

- Additional Palettes

tropical_colors
midcentury_colors
earth_tones
vintage_colors
fresh_colors
cool_tones
monochrome
pastel_colors
natural_colors
vivid_colors
deep_blue_light_blue
navy_blue_purple
cobalt_blue_light_blue
dark_blue_teal
cobalt_blue_aqua
bluna

## Example

import matplotlib.pyplot as plt
from ColorPalettes import ColorPalettes

- Display a specific palette
ColorPalettes.display_palette('twilight_blues', 4)

- Display all palettes in a group
ColorPalettes.display_group_palettes('Tetracolor')

## License

This project is licensed under the MIT License. See the LICENSE file for details.