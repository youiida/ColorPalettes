from colorsys import rgb_to_hsv

import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist, squareform


class ColorPalettes:
    # Tetracolor
    twilight_blues = ['#11225b', '#33b9bb', '#c5edef', '#ed356a']
    vintage_vibes = ['#d46868', '#ffdfa0', '#fbf4ea', '#7ea9aa']
    earthy_tones = ['#89714d', '#9d8981', '#decfc0', '#e3e1da']
    autumn_hues = ['#14a521', '#643b0d', '#ece6cf', '#96a006']
    primary_burst = ['#dd003c', '#315daa', '#3ca03c', '#ffc800']
    muted_greens = ['#7e928d', '#c19a88', '#b1cdbb', '#e4ddd5']
    pastel_dreams = ['#fb80c0', '#99ded6', '#b084e0', '#4a4492']
    neon_flash = ['#db0e5d', '#1eb5d9', '#ffff33', '#59b636']
    royal_purples = ['#625a81', '#d58b6d', '#8e5568', '#e6e5df']
    soft_pinks = ['#e99891', '#4d4d4d', '#edd2d0', '#e6e5df']
    forest_shades = ['#367853', '#5e9594', '#bfcd5a', '#d6974a']
    luxury_blues = ['#1d3d5e', '#b8d0ed', '#7b9098', '#9d8c56']
    earthy_tones = ['#456629', '#9f554f', '#e5dfcf', '#c8d6ba']
    oceanic_vibes = ['#caeff3', '#14518e', '#bbc8d8', '#c59650']
    vintage_charm = ['#a6baae', '#ece0ca', '#967462', '#5d3e3f']
    tropical_sunset = ['#ede1ca', '#40cfd7', '#2a2f33', '#fe7d5a']
    bold_classics = ['#c1123d', '#d1aa44', '#5d0529', '#210307']
    regal_elegance = ['#263460', '#eaaf59', '#efe6d8', '#c63c46']
    soft_japanese = ['#83ba93', '#fcefde', '#f9b693', '#f9c8c0']
    cool_breeze = ['#e9eff4', '#557bb7', '#99d6d6', '#ababdd']
    soft_neutrals = ['#edccc7', '#d2a8aa', '#fcf4e5', '#d1bea3']
    calm_pinks = ['#f9f6f7', '#a53d59', '#d5a8aa', '#582341']
    soft_greys = ['#adafba', '#f77a9f', '#e8e4ec', '#747884']
    vibrant_pinks = ['#fe3781', '#ff77ad', '#ecf660', '#747884']

    # Alt Black
    alt_black = {
        '#1d2131': 'charcoal',
        '#30384e': 'slate',
        '#323942': 'graphite',
        '#0a1c1f': 'midnight',
        '#252525': 'onyx',
        '#271e3d': 'plum_black',
        '#131313': 'jet',
        '#2a3a3a': 'dark_teal',
        '#192a3c': 'navy_black',
        '#072524': 'deep_sea',
        '#3e3a39': 'smoky_black',
        '#07172f': 'midnight_blue',
        '#1e2127': 'steel',
        '#200204': 'black_cherry',
        '#331f2a': 'black_rose',
        '#3e3a46': 'charcoal_purple',
        '#140b26': 'black_violet',
        '#17252f': 'black_ice',
        '#100706': 'ebony',
        '#4c5158': 'slate_gray',
        '#3f3f3d': 'ash',
        '#301a07': 'dark_wood',
        '#263940': 'stormy_sea'
    }

    # Bicolor
    lavender_peach = ['#c3bfd8', '#f4a258']
    blush_gold = ['#d5b4b5', '#dbb426']
    apricot_olive = ['#e5bb8b', '#8b905e']
    ivory_teal = ['#ebe1d2', '#90acaf']
    sage_coral = ['#5e8467', '#c37960']
    lime_pink = ['#bdc681', '#d39aad']
    sky_bronze = ['#6d8eb9', '#a87d40']
    pearl_rose = ['#b9b8c8', '#f8517e']
    mint_mustard = ['#bbdccb', '#abaf4c']
    ochre_blue = ['#e2aa6f', '#697993']
    sand_rust = ['#cdb092', '#a55a51']
    peach_navy = ['#cda59a', '#567b89']
    blue_red = ['#85abd5', '#c64a47']
    lilac_navy = ['#ded4e8', '#454e6b']
    olive_plum = ['#a1ad8f', '#8f819b']
    peach_forest = ['#e19c8f', '#324332']
    sky_coal = ['#a9b9cf', '#1b1e21']
    iron_brown = ['#89989a', '#593c3c']
    cream_teal = ['#cbc3ab', '#37575f']
    gold_navy = ['#cbad40', '#314097']
    ocean_sunset = ['#529eb9', '#e94031']
    forest_rose = ['#4da869', '#e1888b']
    vintage_rose = ['#cf7174', '#0a6395']
    harvest_gold = ['#ccb964', '#24401e']
    desert_sunset = ['#ba9d73', '#cd6319']
    autumn_leaves = ['#764734', '#e8bb4c']
    rustic_red = ['#342a22', '#b94c2e']
    coral_sea = ['#6fbcbf', '#c24243']
    golden_night = ['#ddba58', '#1a387b']
    twilight_orange = ['#e24744', '#2b2648']
    misty_rose = ['#2e4b4e', '#d49ca7']
    sky_garden = ['#335dac', '#9fbd7a']
    earthy_tones_retro = ['#839b67', '#967a66']
    cherry_sky = ['#bb4645', '#57a4d2']
    midnight_fire = ['#283852', '#b73d06']
    olive_bark = ['#a0a77a', '#5d3332']
    teal_sun = ['#447c7f', '#da7f01']
    red_dawn = ['#c34a53', '#c5b052']
    ocean_sunrise = ['#384355', '#f7b334']
    autumn_leaves = ['#39352a', '#df6d56']
    rose_garden = ['#3b4265', '#f7b67e']
    forest_path = ['#131f04', '#578b52']
    woodland_walk = ['#926a52', '#7f8768']
    sunset_boulevard = ['#3b5767', '#e37d7f']
    desert_sand = ['#304c4d', '#f1c08a']
    meadow_green = ['#304b45', '#82b98b']
    urban_sky = ['#3a3a37', '#a1a8a7']
    summer_citrus = ['#08325c', '#f7b134']
    rustic_charm = ['#385f55', '#f3b1a1']
    spring_meadow = ['#303f26', '#f4e342']
    golden_horizon = ['#0b3b53', '#f6b346']
    twilight_sky = ['#374868', '#f6c867']
    deep_sea = ['#304b68', '#4e7a7e']
    lime_twist = ['#363c26', '#f4e842']
    red_velvet = ['#3b3733', '#d84b5a']
    steely_resolve = ['#3d4552', '#a5a7a6']
    soft_petals = ['#302425', '#f7d2c3']
    crimson_flame = ['#7f2a21', '#d84d3a']
    cool_mist = ['#3a5a7d', '#f1d9c6']
    glacial_blue = ['#2d4755', '#d1d1d4']
    autumn_spice = ['#37332b', '#f47e42']
    royal_plum = ['#3b3a5c', '#f1a1b8']
    sunset_and_sky = ['#FFA500', '#0000FF']
    blossom_and_grass = ['#FF00FF', '#00FF00']
    sunshine_and_twilight = ['#FFFF00', '#800080']
    vibrant_sunset = ['#FF007A', '#7A00FF']
    golden_horizon = ['#FFEF00', '#FF7A00']
    aqua_dream = ['#00E0FF', '#0094FF']
    fire_and_ice = ['#FF6400', '#00D8FF']
    golden_sunshine = ['#FFE000', '#FFA200']
    aqua_serenity = ['#00FFA2', '#00E0FF']
    rose_gold = ['#FF0078', '#FFB4A2']

    # Tricolor
    venetian_sunset = ['#99cc99', '#ffcc66', '#cc6600']
    cherry_blossom_petals = ['#f7b578', '#f6c0ab', '#cc929d']
    mountain_range_view = ['#e6d4b3', '#9ab9a1', '#8da766']
    after_the_rain = ['#c0b8ab', '#d4a794', '#94a2a1']
    stone_wall_moss = ['#918987', '#4d4c46', '#d4c6b3']
    calm_lake = ['#b1c4b6', '#94a9b0', '#c3c3c9']
    forest_light_and_shadow = ['#557566', '#8e9a63', '#f5c1ab']
    autumn_leaves_journey = ['#a97760', '#4a5440', '#875667']
    warm_earth_scent = ['#d34604', '#aabc5e', '#d4c492']
    moonlit_sea = ['#4c6a7f', '#e0e2b7', '#d9dad2']
    soft_pastels = ['#e6cccc', '#d4b7a7', '#aac194']
    autumn_breeze = ['#a99a7c', '#7d6a5a', '#78809a']
    aegean_sea = ['#8eabb5', '#c4c6b3', '#61939f']
    morning_light_rays = ['#f0f0f0', '#e0e5cd', '#b5b3ab']
    fruit_orchard = ['#9eacf9', '#ce4f4f', '#81bcc0']
    plum_orchard = ['#a1c179', '#7e9d60', '#5f7051']
    mujirushi = ['#7F0019', '#d8b07b', '#a9a9a9']

    # Additional Palettes
    cool_tones = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78',
                  '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5']
    monochrome = ['#000000', '#333333', '#666666',
                  '#999999', '#cccccc', '#ffffff']
    pastel_colors = ['#ffb3ba', '#ffdfba', '#ffffba', '#baffc9',
                     '#bae1ff', '#d4a5a5', '#d4c5a5', '#d4d4a5', '#a5d4a5', '#a5d4d4']
    natural_colors = ['#8c564b', '#c49c94', '#e377c2', '#f7b6d2',
                      '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']
    vivid_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3',
                    '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999']
    tropical_colors = ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9',
                       '#92a8d1', '#955251', '#b565a7', '#009b77', '#dd4124', '#d65076']
    midcentury_colors = ['#e94b3c', '#6f9fd8', '#944743', '#dbb1cd',
                         '#ec9787', '#00a591', '#6b5b95', '#feb236', '#d64161', '#ff7b25']
    earth_tones = ['#8d6e63', '#d7ccc8', '#a1887f', '#ffccbc',
                   '#bcaaa4', '#ffab91', '#d84315', '#4e342e', '#3e2723', '#bf360c']
    vintage_colors = ['#c0b283', '#6b4226', '#d9bf77', '#8c5e58',
                      '#d9b44a', '#4f6457', '#acd8aa', '#d9b44a', '#75b1a9', '#563838']
    fresh_colors = ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9',
                    '#92a8d1', '#955251', '#b565a7', '#009b77', '#dd4124', '#d65076']
    deep_blue_light_blue = ['#1f77b4', '#aec7e8', '#2ca02c', '#98df8a']
    navy_blue_purple = ['#003f5c', '#7a5195', '#2f4b7c', '#a05195']
    cobalt_blue_light_blue = ['#00509e', '#6baed6', '#31a354', '#a1d99b']
    dark_blue_teal = ['#1b3a4b', '#70a1d7', '#1b998b', '#9fd356']
    cobalt_blue_aqua = ['#004c6d', '#8ecae6', '#2a9d8f', '#b7e4c7']
    bruna = ['#080000', '#88593b', '#ea5415', '#ee7701',
             '#ffdf00', '#737061', '#005192', '#1d7a21']

    all_palette = {
        'twilight_blues': ['#11225b', '#33b9bb', '#c5edef', '#ed356a'],
        'vintage_vibes': ['#d46868', '#ffdfa0', '#fbf4ea', '#7ea9aa'],
        'earthy_tones': ['#89714d', '#9d8981', '#decfc0', '#e3e1da'],
        'autumn_hues': ['#14a521', '#643b0d', '#ece6cf', '#96a006'],
        'primary_burst': ['#dd003c', '#315daa', '#3ca03c', '#ffc800'],
        'muted_greens': ['#7e928d', '#c19a88', '#b1cdbb', '#e4ddd5'],
        'pastel_dreams': ['#fb80c0', '#99ded6', '#b084e0', '#4a4492'],
        'neon_flash': ['#db0e5d', '#1eb5d9', '#ffff33', '#59b636'],
        'royal_purples': ['#625a81', '#d58b6d', '#8e5568', '#e6e5df'],
        'soft_pinks': ['#e99891', '#4d4d4d', '#edd2d0', '#e6e5df'],
        'forest_shades': ['#367853', '#5e9594', '#bfcd5a', '#d6974a'],
        'luxury_blues': ['#1d3d5e', '#b8d0ed', '#7b9098', '#9d8c56'],
        'earthy_tones': ['#e5dfcf', '#c8d6ba', '#456629', '#9f554f'],
        'oceanic_vibes': ['#caeff3', '#14518e', '#bbc8d8', '#c59650'],
        'vintage_charm': ['#a6baae', '#ece0ca', '#967462', '#5d3e3f'],
        'tropical_sunset': ['#ede1ca', '#40cfd7', '#2a2f33', '#fe7d5a'],
        'bold_classics': ['#c1123d', '#d1aa44', '#5d0529', '#210307'],
        'regal_elegance': ['#263460', '#eaaf59', '#efe6d8', '#c63c46'],
        'soft_japanese': ['#83ba93', '#fcefde', '#f9b693', '#f9c8c0'],
        'cool_breeze': ['#e9eff4', '#557bb7', '#99d6d6', '#ababdd'],
        'soft_neutrals': ['#edccc7', '#d2a8aa', '#fcf4e5', '#d1bea3'],
        'calm_pinks': ['#f9f6f7', '#a53d59', '#d5a8aa', '#582341'],
        'soft_greys': ['#adafba', '#f77a9f', '#e8e4ec', '#747884'],
        'vibrant_pinks': ['#fe3781', '#ff77ad', '#ecf660', '#747884'],
        'lavender_peach': ['#c3bfd8', '#f4a258'],
        'blush_gold': ['#d5b4b5', '#dbb426'],
        'apricot_olive': ['#e5bb8b', '#8b905e'],
        'ivory_teal': ['#ebe1d2', '#90acaf'],
        'sage_coral': ['#5e8467', '#c37960'],
        'lime_pink': ['#bdc681', '#d39aad'],
        'sky_bronze': ['#6d8eb9', '#a87d40'],
        'pearl_rose': ['#b9b8c8', '#f8517e'],
        'mint_mustard': ['#bbdccb', '#abaf4c'],
        'ochre_blue': ['#e2aa6f', '#697993'],
        'sand_rust': ['#cdb092', '#a55a51'],
        'peach_navy': ['#cda59a', '#567b89'],
        'blue_red': ['#85abd5', '#c64a47'],
        'lilac_navy': ['#ded4e8', '#454e6b'],
        'olive_plum': ['#a1ad8f', '#8f819b'],
        'peach_forest': ['#e19c8f', '#324332'],
        'sky_coal': ['#a9b9cf', '#1b1e21'],
        'iron_brown': ['#89989a', '#593c3c'],
        'cream_teal': ['#cbc3ab', '#37575f'],
        'gold_navy': ['#cbad40', '#314097'],
        'ocean_sunset': ['#529eb9', '#e94031'],
        'forest_rose': ['#4da869', '#e1888b'],
        'vintage_rose': ['#cf7174', '#0a6395'],
        'harvest_gold': ['#ccb964', '#24401e'],
        'desert_sunset': ['#ba9d73', '#cd6319'],
        'autumn_leaves': ['#39352a', '#df6d56'],
        'rustic_red': ['#342a22', '#b94c2e'],
        'coral_sea': ['#6fbcbf', '#c24243'],
        'golden_night': ['#ddba58', '#1a387b'],
        'twilight_orange': ['#e24744', '#2b2648'],
        'misty_rose': ['#2e4b4e', '#d49ca7'],
        'sky_garden': ['#335dac', '#9fbd7a'],
        'earthy_tones_retro': ['#839b67', '#967a66'],
        'cherry_sky': ['#bb4645', '#57a4d2'],
        'midnight_fire': ['#283852', '#b73d06'],
        'olive_bark': ['#a0a77a', '#5d3332'],
        'teal_sun': ['#447c7f', '#da7f01'],
        'red_dawn': ['#c34a53', '#c5b052'],
        'ocean_sunrise': ['#384355', '#f7b334'],
        'rose_garden': ['#3b4265', '#f7b67e'],
        'forest_path': ['#131f04', '#578b52'],
        'woodland_walk': ['#926a52', '#7f8768'],
        'sunset_boulevard': ['#3b5767', '#e37d7f'],
        'desert_sand': ['#304c4d', '#f1c08a'],
        'meadow_green': ['#304b45', '#82b98b'],
        'urban_sky': ['#3a3a37', '#a1a8a7'],
        'summer_citrus': ['#08325c', '#f7b134'],
        'rustic_charm': ['#385f55', '#f3b1a1'],
        'spring_meadow': ['#303f26', '#f4e342'],
        'golden_horizon': ['#0b3b53', '#f6b346'],
        'twilight_sky': ['#374868', '#f6c867'],
        'deep_sea': ['#304b68', '#4e7a7e'],
        'lime_twist': ['#363c26', '#f4e842'],
        'red_velvet': ['#3b3733', '#d84b5a'],
        'steely_resolve': ['#3d4552', '#a5a7a6'],
        'soft_petals': ['#302425', '#f7d2c3'],
        'crimson_flame': ['#7f2a21', '#d84d3a'],
        'cool_mist': ['#3a5a7d', '#f1d9c6'],
        'glacial_blue': ['#2d4755', '#d1d1d4'],
        'autumn_spice': ['#37332b', '#f47e42'],
        'royal_plum': ['#3b3a5c', '#f1a1b8'],
        'sunset_and_sky': ['#FFA500', '#0000FF'],
        'blossom_and_grass': ['#FF00FF', '#00FF00'],
        'sunshine_and_twilight': ['#FFFF00', '#800080'],
        'vibrant_sunset': ['#FF007A', '#7A00FF'],
        'aqua_dream': ['#00E0FF', '#0094FF'],
        'fire_and_ice': ['#FF6400', '#00D8FF'],
        'golden_sunshine': ['#FFE000', '#FFA200'],
        'aqua_serenity': ['#00FFA2', '#00E0FF'],
        'rose_gold': ['#FF0078', '#FFB4A2'],
        'venetian_sunset': ['#99cc99', '#ffcc66', '#cc6600'],
        'cherry_blossom_petals': ['#f7b578', '#f6c0ab', '#cc929d'],
        'mountain_range_view': ['#e6d4b3', '#9ab9a1', '#8da766'],
        'after_the_rain': ['#c0b8ab', '#d4a794', '#94a2a1'],
        'stone_wall_moss': ['#918987', '#4d4c46', '#d4c6b3'],
        'calm_lake': ['#b1c4b6', '#94a9b0', '#c3c3c9'],
        'forest_light_and_shadow': ['#557566', '#8e9a63', '#f5c1ab'],
        'autumn_leaves_journey': ['#a97760', '#4a5440', '#875667'],
        'warm_earth_scent': ['#d34604', '#aabc5e', '#d4c492'],
        'moonlit_sea': ['#4c6a7f', '#e0e2b7', '#d9dad2'],
        'soft_pastels': ['#e6cccc', '#d4b7a7', '#aac194'],
        'autumn_breeze': ['#a99a7c', '#7d6a5a', '#78809a'],
        'aegean_sea': ['#8eabb5', '#c4c6b3', '#61939f'],
        'morning_light_rays': ['#f0f0f0', '#e0e5cd', '#b5b3ab'],
        'fruit_orchard': ['#9eacf9', '#ce4f4f', '#81bcc0'],
        'plum_orchard': ['#a1c179', '#7e9d60', '#5f7051'],
        'mujirushi': ['#7F0019', '#d8b07b', '#e1c8a8'],
        'cool_tones': ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5'],
        'monochrome': ['#000000', '#333333', '#666666', '#999999', '#cccccc', '#ffffff'],
        'pastel_colors': ['#ffb3ba', '#ffdfba', '#ffffba', '#baffc9', '#bae1ff', '#d4a5a5', '#d4c5a5', '#d4d4a5', '#a5d4a5', '#a5d4d4'],
        'natural_colors': ['#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5'],
        'vivid_colors': ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999'],
        'tropical_colors': ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9', '#92a8d1', '#955251', '#b565a7', '#009b77', '#dd4124', '#d65076'],
        'midcentury_colors': ['#e94b3c', '#6f9fd8', '#944743', '#dbb1cd', '#ec9787', '#00a591', '#6b5b95', '#feb236', '#d64161', '#ff7b25'],
        'earth_tones': ['#8d6e63', '#d7ccc8', '#a1887f', '#ffccbc', '#bcaaa4', '#ffab91', '#d84315', '#4e342e', '#3e2723', '#bf360c'],
        'vintage_colors': ['#c0b283', '#6b4226', '#d9bf77', '#8c5e58', '#d9b44a', '#4f6457', '#acd8aa', '#d9b44a', '#75b1a9', '#563838'],
        'fresh_colors': ['#ff6f61', '#6b5b95', '#88b04b', '#f7cac9', '#92a8d1', '#955251', '#b565a7', '#009b77', '#dd4124', '#d65076'],
        'deep_blue_light_blue': ['#1f77b4', '#aec7e8', '#2ca02c', '#98df8a'],
        'navy_blue_purple': ['#003f5c', '#7a5195', '#2f4b7c', '#a05195'],
        'cobalt_blue_light_blue': ['#00509e', '#6baed6', '#31a354', '#a1d99b'],
        'dark_blue_teal': ['#1b3a4b', '#70a1d7', '#1b998b', '#9fd356'],
        'cobalt_blue_aqua': ['#004c6d', '#8ecae6', '#2a9d8f', '#b7e4c7'],
        'bruna': ['#080000', '#88593b', '#ea5415', '#ee7701', '#ffdf00', '#737061', '#005192', '#1d7a21']
    }

    @staticmethod
    def get_palette(palette_name, num_colors=None):
        reverse = False

        if palette_name.startswith('r_'):
            reverse = True
            palette_name = palette_name[2:]

        palette = getattr(ColorPalettes, palette_name, None)
        if num_colors is None:
            num_colors = len(palette)
        if palette is None:
            raise ValueError(f"Palette '{palette_name}' not found.")

        if reverse:
            if isinstance(palette, list):
                palette = palette[::-1]
            elif isinstance(palette, dict):
                palette = dict(reversed(list(palette.items())))

        if isinstance(palette, list):
            if num_colors <= len(palette):
                return palette[:num_colors]
            else:
                # 繰り返して必要な色数を満たす
                return (palette * (num_colors // len(palette) + 1))[:num_colors]
        elif isinstance(palette, dict):
            keys = list(palette.keys())
            if num_colors <= len(keys):
                return {k: palette[k] for k in keys[:num_colors]}
            else:
                extended_keys = (
                    keys * (num_colors // len(keys) + 1))[:num_colors]
                return {k: palette[k] for k in extended_keys}

    @staticmethod
    def display_palette(palette_name, num_colors):
        palette = ColorPalettes.get_palette(palette_name, num_colors)
        fig, ax = plt.subplots(figsize=(num_colors, 2))
        if isinstance(palette, list):
            for i, color in enumerate(palette):
                ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
        elif isinstance(palette, dict):
            for i, (color, name) in enumerate(palette.items()):
                ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
                ax.text(i + 0.5, 0.5, name, ha='center',
                        va='center', fontsize=8, color='white')
        ax.set_xlim(0, num_colors)
        ax.set_ylim(0, 1)
        ax.axis('off')
        plt.show()

    def get_group_name():
        return ['Tetracolor', 'Alt Black', 'Bicolor', 'Tricolor', 'Additional Palettes']

    @staticmethod
    def display_group_palettes(group_name):
        group_palettes = {
            'Tetracolor': ['twilight_blues', 'vintage_vibes', 'earthy_tones', 'autumn_hues', 'primary_burst', 'muted_greens', 'pastel_dreams', 'neon_flash', 'royal_purples', 'soft_pinks', 'forest_shades', 'luxury_blues', 'earthy_tones', 'oceanic_vibes', 'vintage_charm', 'tropical_sunset', 'bold_classics', 'regal_elegance', 'soft_japanese', 'cool_breeze', 'soft_neutrals','calm_pinks','soft_greys','vibrant_pinks'],
            'Alt Black': ['alt_black'],
            'Bicolor': ['lavender_peach', 'blush_gold', 'apricot_olive', 'ivory_teal', 'sage_coral', 'lime_pink', 'sky_bronze', 'pearl_rose', 'mint_mustard', 'ochre_blue', 'sand_rust', 'peach_navy', 'blue_red', 'lilac_navy', 'olive_plum', 'peach_forest', 'sky_coal', 'iron_brown', 'cream_teal', 'gold_navy', 'ocean_sunset', 'forest_rose', 'vintage_rose', 'harvest_gold', 'desert_sunset', 'autumn_leaves', 'rustic_red', 'coral_sea', 'golden_night', 'twilight_orange', 'misty_rose', 'sky_garden', 'earthy_tones_retro', 'cherry_sky', 'midnight_fire', 'olive_bark', 'teal_sun', 'red_dawn', 'ocean_sunrise', 'autumn_leaves', 'rose_garden', 'forest_path', 'woodland_walk', 'sunset_boulevard', 'desert_sand', 'meadow_green', 'urban_sky', 'summer_citrus', 'rustic_charm', 'spring_meadow', 'golden_horizon', 'twilight_sky', 'deep_sea', 'lime_twist', 'red_velvet', 'steely_resolve', 'soft_petals', 'crimson_flame', 'cool_mist', 'glacial_blue', 'autumn_spice', 'royal_plum', 'vibrant_sunset', 'golden_horizon', 'aqua_dream', 'fire_and_ice', 'golden_sunshine', 'aqua_serenity', 'rose_gold'],
            'Tricolor': ['venetian_sunset', 'cherry_blossom_petals', 'mountain_range_view', 'after_the_rain', 'stone_wall_moss', 'calm_lake', 'forest_light_and_shadow', 'autumn_leaves_journey', 'warm_earth_scent', 'moonlit_sea', 'soft_pastels', 'autumn_breeze', 'aegean_sea', 'morning_light_rays', 'fruit_orchard', 'plum_orchard', 'mujirushi'],
            'Additional Palettes': ['cool_tones', 'monochrome', 'pastel_colors', 'natural_colors', 'vivid_colors', 'tropical_colors', 'midcentury_colors', 'earth_tones', 'vintage_colors', 'fresh_colors', 'deep_blue_light_blue', 'navy_blue_purple', 'cobalt_blue_light_blue', 'dark_blue_teal', 'cobalt_blue_aqua', 'bruna']
        }

        if group_name not in group_palettes:
            raise ValueError(f"Group '{group_name}' not found.")

        palettes = group_palettes[group_name]
        num_palettes = len(palettes)
        fig, axes = plt.subplots(
            num_palettes, 1, figsize=(10, 2 * num_palettes))

        if num_palettes == 1:
            axes = [axes]

        for ax, palette_name in zip(axes, palettes):
            palette = getattr(ColorPalettes, palette_name)
            if isinstance(palette, list):
                for i, color in enumerate(palette):
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
            elif isinstance(palette, dict):
                for i, (color, name) in enumerate(palette.items()):
                    ax.add_patch(plt.Rectangle((i, 0), 1, 1, color=color))
                    ax.text(i + 0.5, 0.5, name, ha='center',
                            va='center', fontsize=8, color='white')
            ax.set_xlim(0, len(palette))
            ax.set_ylim(0, 1)
            ax.axis('off')
            ax.set_title(palette_name, loc='left', fontsize=12, pad=10)

        plt.tight_layout()
        plt.show()