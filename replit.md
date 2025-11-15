# Ultimate Pokédex

## Overview
A comprehensive, feature-packed Pokédex with an Apple liquid glass aesthetic. Provides complete information about all 1000+ Pokémon using the PokéAPI.

## Technology Stack
- **Backend**: Python Flask (proxies PokéAPI requests)
- **Frontend**: Single HTML file with vanilla JavaScript
- **API**: PokéAPI (https://pokeapi.co/api/v2/)
- **Styling**: CSS3 with backdrop-filter for glass morphism
- **Storage**: LocalStorage for team and preferences

## Architecture
- `app.py` - Flask backend that proxies all PokéAPI requests to avoid CORS issues
- `index.html` - Complete frontend application with all features
- Backend runs on port 5000, serving both the HTML and API endpoints

## Features

### Core Features
- **Complete Pokédex**: Browse all 1000+ Pokémon with pixelated sprites
- **Detailed Pokémon View**: 
  - Base stats with visual progress bars
  - Abilities (normal and hidden)
  - Types with effectiveness matchups
  - Evolution chains with methods
  - **Detailed Move Information**: Power, accuracy, PP, damage class, type, and descriptions
  - Physical data (height, weight)
  - Game data (generation, habitat, capture rate)
  - Shiny sprite toggle
- **Search & Filter**: By name, ID, type (18 types), generation (I-IX), with sorting
- **Type System**: Complete type effectiveness chart showing weaknesses, resistances, and immunities
- **Comparison Tool**: Compare two Pokémon side-by-side with stat highlighting
- **Database Features**: Move database (100 moves) and ability encyclopedia (100 abilities)

### Team Builder
Enhanced team building with full customization:
- Save up to 6 Pokémon
- **Nicknames**: Custom names for each Pokémon
- **EV Editor**: Set Effort Values (0-252) for all 6 stats (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed)
- **Export**: Download team as JSON file
- Persistent storage using LocalStorage

### Visual Features
- Clean, minimal UI with compact controls
- Pixelated sprites on main grid for retro aesthetic
- High-quality official artwork in detail view
- Apple liquid glass design with frosted glass effects
- Dark/light mode toggle
- Smooth animations and transitions
- Responsive grid layout

## UI Design Philosophy
- **Less Clutter**: Compact buttons, shorter labels, tighter spacing
- **Clean Typography**: Small, readable fonts (11-14px)
- **Efficient Layout**: Dense but organized information presentation
- **Glass Morphism**: Subtle backdrop blur and transparency effects

## API Endpoints (Backend)
- `GET /` - Serve HTML
- `GET /api/pokemon?limit=N` - List Pokémon
- `GET /api/pokemon/<id>` - Pokémon details
- `GET /api/pokemon-species/<id>` - Species information
- `GET /api/evolution-chain/<id>` - Evolution data
- `GET /api/move?limit=N` - Move database
- `GET /api/move/<id>` - Move details
- `GET /api/ability?limit=N` - Ability list
- `GET /api/ability/<id>` - Ability details

## Project Structure
```
.
├── app.py           # Flask backend
├── index.html       # Frontend application
└── replit.md        # Documentation
```

## User Preferences
- Theme (dark/light) stored in LocalStorage
- Team (6 slots with nicknames and EVs) stored in LocalStorage

## Recent Changes
- 2025-11-14: Switched to pixelated sprites on main grid for retro aesthetic
- 2025-11-14: Enhanced move information with power, accuracy, PP, damage class, and descriptions
- 2025-11-14: Added Flask backend to proxy PokéAPI requests (fixes CORS issues)
- 2025-11-14: Redesigned UI to be cleaner and less cluttered
- 2025-11-14: Enhanced team builder with nicknames and EV editor
- 2025-11-14: Removed stat filters and damage calculator per user request
