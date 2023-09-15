/**
 * Welcome! This is basic JavaScript Discord bot. Good work!
 * This repository is created by mEt0_. Concact me (Discord): meto1558
 */

// First, import the discord.js Classes, Enums etc.
const { Client, GatewayIntentBits } = require("discord.js");

// Create a bot object
const bot = new Client({
    intents: [ // Enter Intents for the bot to work properly
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers,
        GatewayIntentBits.GuildVoiceStates // This Intent allows the bot to join and manage voice channels
    ]
});

// Bot's ready listener
bot.on("ready", async () => { // If you don't know what "=>" does, you can use it in "async function"
    console.log("Bot is ready!");
});

// Message create listener or command builder (discord.js does not have a listener like "bot.create_command" to create prefix based commands)
bot.on("messageCreate", async (message) => {
    // Check if the message owner is a bot
    if (message.author.bot) return;

    // Check what is written in the resulting message
    if (message.content.toLowerCase() == "hello") {
        await message.reply("Hi!");
    }
    // Create a basic command
    if (message.content.toLowerCase() == "(YOUR_BOT_PREFIX_HERE)yo") {
        await message.channel.send("Hello, how are you?");
    }
});

// Connect to Discord Gateway
bot.login("YOUR_BOT_TOKEN_HERE");

/**
 * Finally, run the bot, use this command: node your_file_name.js (REQUIRED: Node.js 16.11.0 or higher, npm or yarn Package Manager)
 */