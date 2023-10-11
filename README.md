# Perk Configuration Readme

This repository contains the configuration files for managing perks in a game server. It is essential for determining the version of the perks on the server. If you've added new perks to the list, make sure to increase the version number, so players receive the updated perk list when they join the server.

## Main Settings

### Clearing Player Points

- `clearPlayersPoints`: Set to 1 to reset unused points when a player dies, or 0 to keep points as they are.

### Decreasing Points

- `enableDeacreasePoints`: If enabled, player points will decrease by a certain percentage defined in the settings below when `clearPlayersPoints` is on.

- `PointsDecreaseAfterDeath`: Configure the percentage decrease for each type of experience. Values range from 0 to 1 (e.g., 0.3 for 30% decrease) upon death.

### Clearing Perks After a Specific Number of Deaths

- `ClearPlayerPerkUsingPenalty`: Set to 1 to enable perk reset after a certain number of player deaths, or 0 to disable it.

- `PlayerCountDeathToPenalty`: Specify the number of deaths required for perk reset.

### Random Perk Reset

- `clearPerkUsingRandom`: Set to 1 to enable random perk resets based on the count defined in the settings below.

- `clearPerkUsingRandom_count`: Specify the number of perks that will be randomly reset.

### Clearing Perks Based on Chance

- `clearPerkUsingChance`: Set to 1 to reset activated perks when a player dies, or 0 to keep them. When disabled, all perks will reset as if they have a 100% reset chance. Note that dependent perks may also reset.

- Perk Option: `chanceToClear`: Define a chance from 0 to 1 for individual perk resets. Default is 1 if not specified in the JSON settings.

## Log Profiles

- `enableLogsProfile`: Set to 1 to enable logging, or 0 to disable it.

## Initial Experience Values

Set the initial values for various categories of experience in case perks are reset or when new players join:

- `StartingFishing`
- `StartingHunting`
- `StartingMedical`
- `StartingEngineering`
- `StartingGardening`
- `StartingEndurance`

## Experience Modifiers

Each category of experience can be modified by a multiplier:

- `HuntingModifier`
- `MedicalModifier`
- `EngineeringModifier`
- `GardeningModifier`
- `FishingModifier`

The total experience gained in each category will be multiplied by the respective modifier.

## Perk Rotten Eat Settings

Configure settings for perks related to food preparation:

### Bad Eat Prepare Tool

- List of tools that can be used for bad food preparation.

### Bad Eat Prepare Meat

- List of meats that can be prepared poorly.

### Bad Eat Prepare Fish

- List of fish that can be prepared poorly.

### Bad Eat Prepare Fruit

- List of fruits and vegetables that can be prepared poorly.

Please refer to the respective sections in your configuration files for detailed information and customization.

---

Feel free to update this README with any additional information or instructions as needed for your project.
