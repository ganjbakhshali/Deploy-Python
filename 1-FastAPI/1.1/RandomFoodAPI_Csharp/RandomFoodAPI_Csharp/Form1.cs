using System;
using System.Drawing;
using System.Globalization;
using System.IO;
using System.Net.Http;
using System.Text.Json;
using System.Windows.Forms;

namespace RandomFoodAPI_Csharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            pbox_food.SizeMode = PictureBoxSizeMode.Zoom;
        }

        public class FoodResponse
        {
            public string image { get; set; }
        }

        private async void btn_getPic_Click(object sender, EventArgs e)
        {
            try
            {
                using HttpClient client = new HttpClient();

                string json = await client.GetStringAsync(
                    "https://foodish-api.com/api"
                );

                FoodResponse food =
                    JsonSerializer.Deserialize<FoodResponse>(json);

                if (food == null || string.IsNullOrEmpty(food.image))
                {
                    MessageBox.Show("Invalid API response");
                    return;
                }

                string[] parts = food.image.Split('/');

                string foodName = parts[parts.Length - 2];

                lbl_foodName.Text =
                    CultureInfo.CurrentCulture.TextInfo
                    .ToTitleCase(
                        foodName.Replace("-", " ")
                    );

                byte[] imageBytes =
                    await client.GetByteArrayAsync(food.image);

                using MemoryStream ms =
                    new MemoryStream(imageBytes);

                Image img = Image.FromStream(ms);

                pbox_food.Image = img;
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    ex.Message,
                    "Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error
                );
            }
        }
    }
}