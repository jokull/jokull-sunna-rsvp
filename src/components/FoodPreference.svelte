<script>
  export let value;
</script>

<label class="block">
  <span>&nbsp;</span>
  <select bind:value class="block w-full mt-1 border-0 bg-transparent select">
    <option value="vegan">Vegan</option>
    <option value="pescatarian">Fiskur</option>
    <option value="meat">Kjöt</option>
  </select>
</label>
