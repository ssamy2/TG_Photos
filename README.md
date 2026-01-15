# Telegram Gift Images

Free collection of Telegram gift images in WebP format.

## Usage

All images are **free to use** for any purpose.

### Access by Gift ID

```
by_id/{gift_id}.webp
```

Example: `by_id/5936013938331222567.webp` (Plush Pepe)

### Access by Gift Name

```
by_name/{short_name}.webp
```

Example: `by_name/plush_pepe.webp`

## Files

- `by_id/` - Images named by gift ID (123 images)
- `by_name/` - Images named by short name (123 images)
- `Gifts_Details.json` - Full gift data with names and IDs

## Gift Data Structure

```json
{
  "upgraded": [
    {
      "full_name": "Plush Pepe",
      "short_name": "plush_pepe",
      "regular_id": "5936013938331222567"
    }
  ],
  "unupgraded": [
    {
      "full_name": "Torch",
      "short_name": "torch",
      "id": "5999277561060787166"
    }
  ]
}
```

## License

Free to use. No attribution required.
