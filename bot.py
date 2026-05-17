import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="+", intents=intents)

# IDs des deux membres autorisés
ALLOWED_USERS = [1366070003379601500]  # Remplace par les vrais IDs

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def renew(ctx):
    guild = ctx.guild
    await ctx.send("🔄 Renouvellement de tous les salons en cours...")
    print("[INFO] Début du renouvellement des salons...")

    for channel in list(guild.channels):
        category = channel.category
        position = channel.position
        name = channel.name

        print(f"[INFO] Traitement du salon : {name} ({channel.type})")

        # Ignore les catégories elles-mêmes
        if isinstance(channel, discord.CategoryChannel):
            print(f"[INFO] Ignoré : {name} est une catégorie")
            continue

        # Ignore les forums si besoin
        if isinstance(channel, discord.ForumChannel):
            print(f"[INFO] Ignoré : {name} est un forum")
            continue

        # Ignore les salons communautaires requis
        if isinstance(channel, discord.TextChannel) and channel.is_news():
            print(f"[INFO] Ignoré : {name} est un salon obligatoire pour communauté")
            continue

        # Prépare les permissions : tout le monde bloqué
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False)}

        # Autorise les deux membres
        for user_id in ALLOWED_USERS:
            member = guild.get_member(user_id)
            if member:
                if isinstance(channel, discord.VoiceChannel) or isinstance(channel, discord.StageChannel):
                    overwrites[member] = discord.PermissionOverwrite(connect=True, speak=True)
                else:
                    overwrites[member] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

        # Sauvegarde infos spécifiques
        topic = getattr(channel, "topic", None)
        bitrate = getattr(channel, "bitrate", 64000)
        user_limit = getattr(channel, "user_limit", 0)
        nsfw = getattr(channel, "nsfw", False)

        # Supprime l'ancien salon avec gestion des erreurs
        try:
            await channel.delete()
            print(f"[INFO] Salon {name} supprimé")
        except discord.HTTPException as e:
            print(f"[WARN] Impossible de supprimer {name} : {e}")
            continue

        # Recrée le salon selon le type
        if isinstance(channel, discord.TextChannel):
            new_channel = await guild.create_text_channel(
                name=name,
                overwrites=overwrites,
                category=category,
                position=position,
                topic=topic,
                nsfw=nsfw
            )
        elif isinstance(channel, discord.VoiceChannel):
            new_channel = await guild.create_voice_channel(
                name=name,
                overwrites=overwrites,
                category=category,
                position=position,
                bitrate=bitrate,
                user_limit=user_limit
            )
        elif isinstance(channel, discord.StageChannel):
            new_channel = await guild.create_stage_channel(
                name=name,
                overwrites=overwrites,
                category=category,
                position=position
            )

        print(f"[SUCCESS] Salon {name} recréé avec succès !")

    print("✅ Tous les salons renouvelables ont été traités.")
    print("[INFO] Renouvellement terminé.")

bot.run("MTQxNzI1MDY5NTUzODY3NTczMg.GCCbfO.qmbX1WSqwmJT2WtbrtZVGSj0eU0Np9TmCplVAQ")
