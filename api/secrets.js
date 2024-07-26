export default function handler(req, res) {
  res.status(200).json({
    CONFIDENTIAL: process.env.CONFIDENTIAL,
    UTTV: process.env.UTTV,
    SECRET_KEY: process.env.SECRET_KEY
  });
}
