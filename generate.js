const fs = require('fs');
const { exec } = require('child_process');
const gTTS = require('gtts');

const text = 'مرحباً بكم في قناتنا. لا تنسوا الإعجاب والاشتراك.';
const audioFile = 'voice.mp3';
const videoFile = 'video.mp4';
const imageFile = 'background.jpg';

const gtts = new gTTS(text, 'ar');
gtts.save(audioFile, (err) => {
  if (err) {
    console.error('❌ فشل إنشاء الصوت:', err);
    process.exit(1);
  }
  console.log('✅ تم إنشاء الصوت');

  const cmd = `ffmpeg -loop 1 -i ${imageFile} -i ${audioFile} -c:v libx264 -c:a aac -b:a 192k -shortest -y ${videoFile}`;
  exec(cmd, (error, stdout, stderr) => {
    if (error) {
      console.error('❌ فشل إنشاء الفيديو:', stderr);
      process.exit(1);
    } else {
      console.log('✅ تم إنشاء الفيديو بنجاح!');
    }
  });
});
